import mlhp, math

D = 3

print( "1. Setting up mesh and basis", flush=True )

degree = 3
treedepth = 1
alpha = 1e-4

Lx, Ly, Lz, t, pi = 1, 1, 1, 0.2, math.pi
term1 = f"cos(2*{pi}*x/{Lx}) * sin(2*{pi}*y/{Ly})"
term2 = f"cos(2*{pi}*y/{Ly}) * sin(2*{pi}*z/{Lz})"
term3 = f"cos(2*{pi}*z/{Lz}) * sin(2*{pi}*x/{Lx})"

domain = mlhp.implicitFunction(3, f"abs({term1} + {term2} + {term3}) < {t}")

grid = mlhp.makeGrid(nelements=[20] * D, lengths=[1.9] * D, origin=[-0.45] * D)
print(grid)

grid = mlhp.makeRefinedGrid(mlhp.filterCells(grid, domain, nseedpoints=degree + 2))
basis = mlhp.makeHpTrunkSpace(grid, degrees=degree, nfields=D)

print(grid)
print(basis)

print( "2. Computing dirichlet boundary conditions", flush=True )

left = mlhp.integrateDirichletDofs([mlhp.makeConstantFunction(D, 0.0)]*3, basis, [0])
right = mlhp.integrateDirichletDofs(mlhp.makeConstantFunction(D, 1e-3), basis, [1], ifield=0)

dirichlet=mlhp.combineDirichletDofs([left, right])

print( "3. Setting up physics", flush=True )

E = mlhp.makeConstantFunction( D, 200 * 1e9 )
nu = mlhp.makeConstantFunction( D, 0.3 )
rhs = mlhp.makeConstantFunction( D, [0.0, 0.0, 0] )

kinematics = mlhp.makeSmallStrainKinematics( D ) 
constitutive = mlhp.makeIsotropicElasticMaterial( E, nu )
integrand = mlhp.makeIntegrand( kinematics, constitutive, rhs )

print( "4. Allocating linear system", flush=True )

matrix = mlhp.allocateUnsymmetricSparseMatrix( basis, dirichlet[0] )
vector = mlhp.allocateVectorWithSameSize( matrix )

print(matrix)

print( "5. Integrating linear system", flush=True )

#quadrature = mlhp.makeSpaceTreeQuadrature(domain, depth=treedepth, epsilon=alpha)
quadrature = mlhp.makeMomentFittingQuadrature(domain, depth=treedepth, epsilon=alpha)

mlhp.integrateOnDomain( basis, integrand, [matrix, vector], 
    dirichletDofs=dirichlet, quadrature=quadrature )

print( "6. Solving linear system", flush=True )

P = mlhp.makeAdditiveSchwarzPreconditioner( matrix, basis, dirichlet[0] )
#P = mlhp.makeDiagonalPreconditioner( matrix )

interiorDofs, norms = mlhp.cg( matrix, vector, preconditioner=P, maxit=10000, residualNorms=True )

del matrix, P

allDofs = mlhp.inflateDofs( interiorDofs, dirichlet )

print( "7. Postprocessing solution", flush=True )

processors = [mlhp.makeSolutionProcessor( D, allDofs, "Displacement" ),
              mlhp.makeVonMisesProcessor( allDofs, kinematics, constitutive ),
              mlhp.makeFunctionProcessor( domain )]

gridmesh = mlhp.createGridOnCells(mlhp.degreeOffsetResolution(basis), mlhp.PostprocessTopologies.Volumes)
surfmesh = mlhp.createMarchingCubesBoundary(domain, [degree + 2]*D)

gridwriter = mlhp.PVtuOutput( filename="outputs/gyroid_mesh" )
surfwriter = mlhp.PVtuOutput( filename="outputs/gyroid_surf" )
            
mlhp.writeBasisOutput(basis, gridmesh, gridwriter, processors)
mlhp.writeBasisOutput(basis, surfmesh, surfwriter, processors)
