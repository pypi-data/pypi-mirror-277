// This file is part of the mlhp project. License: See LICENSE

#ifndef MLHP_BINDINGS_HELPER_HPP
#define MLHP_BINDINGS_HELPER_HPP

#include <functional>

#include "mlhp/core/alias.hpp"

namespace mlhp::bindings
{

template<typename FunctionType, typename Tag = void> class FunctionWrapper;

template<typename ReturnType, typename... Arguments, typename Tag>
class FunctionWrapper<std::function<ReturnType( Arguments... )>, Tag>
{
public:
    using FunctionType = ReturnType( Arguments... );

    FunctionWrapper( ) = default;

    FunctionWrapper( const std::function<FunctionType>& function ) : 
        function_( function ) 
    { }
    
    FunctionWrapper( std::function<FunctionType>&& function ) : 
        function_( std::move( function ) ) 
    { }

    operator std::function<FunctionType>( ) const
    {
        return function_;
    }

    std::function<FunctionType> get( ) const
    {
        return function_;
    }

    ReturnType call( Arguments&&... args )
    { 
        return function_( std::forward<Arguments>( args ) ... ); 
    }

private:
    std::function<FunctionType> function_;
};

template<typename Function>
inline auto wrapFunction( Function&& function )
{
    auto stdfunction = std::function { std::forward<Function>( function ) };

    return FunctionWrapper<decltype(stdfunction)> { std::move( stdfunction ) };
}

template<size_t D>
using IntegrationOrderDeterminorWrapper = FunctionWrapper<QuadratureOrderDeterminor<D>>;

template<size_t D>
using ScalarFunctionWrapper = FunctionWrapper<spatial::ScalarFunction<D>>;

template<size_t I, size_t O = I>
using VectorFunctionWrapper = FunctionWrapper<spatial::VectorFunction<I, O>>;

template<size_t D>
using SpatialParameterFunctionWrapper = FunctionWrapper<spatial::ParameterFunction<D>>;

struct RealFunctionTag { };

using RealFunctionWrapper = FunctionWrapper<RealFunction, RealFunctionTag>;
using RealFunctionWithDerivativeWrapper = FunctionWrapper<RealFunctionWithDerivative, RealFunctionTag>;

template<size_t D>
using ImplicitFunctionWrapper = FunctionWrapper<ImplicitFunction<D>>;

template<size_t D>
using RefinementFunctionWrapper = FunctionWrapper<RefinementFunction<D>>;

using LinearOperatorWrapper = FunctionWrapper<linalg::LinearOperator>;

template<size_t D>
using ResolutionDeterminorWrapper = FunctionWrapper<ResolutionDeterminor<D>>;

template<size_t D>
using PostprocessingMeshCreatorWrapper = FunctionWrapper<PostprocessingMeshCreator<D>>;

//using SparseSolverWrapper = std::function<DoubleVector( const linalg::AbsSparseMatrix&, DoubleVector& )>;

//! Wrapper for std::vector<double> to prevent conversions to python
class DoubleVector
{
    std::vector<double> data_;
public:
    template<typename... Args>
    DoubleVector( Args&&... args ) : 
        data_( std::forward<Args>( args )... )
    { }

    std::vector<double>& get( )
    {
        return data_;
    }

    const std::vector<double>& get( ) const
    {
        return data_;
    }

    size_t size( ) const
    {
        return data_.size( );
    }
};

class ScalarDouble
{
    double value_;

public:
    explicit ScalarDouble( ) : ScalarDouble { 0.0 } { }
    explicit ScalarDouble( double value ) : value_ { value } { }

    double& get( ) { return value_; }
    const double& get( ) const { return value_; }
};

template<size_t D>
auto add( const std::string& str )
{
    return str + std::to_string( D ) + "D";
}

} // mlhp::bindings

#endif // MLHP_BINDINGS_HELPER_HPP

