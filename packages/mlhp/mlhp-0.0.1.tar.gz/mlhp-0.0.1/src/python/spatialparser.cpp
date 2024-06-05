// This file is part of the mlhp project. License: See LICENSE

#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

#include "helper.hpp"
#include "mlhp/core/spatial.hpp"

namespace mlhp::bindings
{
namespace parser
{

// Define expressions
struct Constant
{
    double value;

    static std::optional<Constant> create( const std::vector<std::string>& expression, size_t )
    {
        return expression[0] == "Constant" ? std::optional<Constant> { Constant { std::stod( expression[1] ) } } : std::nullopt;
    }
};

struct Input
{
    size_t index;

    static std::optional<Input> create( const std::vector<std::string>& expression, size_t ndim )
    {
        if( expression[0] == "Input" )
        {
            auto index = std::stoi( expression[1] );
            auto intdim = static_cast<int>( ndim );

            MLHP_CHECK( index >= 0 && index < intdim, "Invalid input variable index " + std::to_string( index )
                + ". Must be at least 0 and smaller than ndim (" + std::to_string( ndim ) + ")." );

            return Input { static_cast<size_t>( index ) };
        }

        return std::nullopt;
    }
};

struct UnaryOp
{
    long index;
    std::function<double(double)> op;

    static std::optional<UnaryOp> create( const std::vector<std::string>& expr, size_t )
    {
        if( ( expr[0] == "Call" || expr[0] == "UnaryOp" ) && expr.size( ) == 3 )
        {
            using StdPair = std::pair<const char*, double(*)(double)>;

            auto stdfunctions = std::array
            {
                StdPair { "abs"   , std::abs    }, StdPair { "exp"   , std::exp    }, StdPair { "exp2"  , std::exp2  },
                StdPair { "expm1" , std::expm1  }, StdPair { "log"   , std::log    }, StdPair { "log10" , std::log10 },
                StdPair { "log2"  , std::log2   }, StdPair { "log1p" , std::log1p  }, StdPair { "sqrt"  , std::sqrt  },
                StdPair { "qbrt"  , std::cbrt   }, StdPair { "sin"   , std::sin    }, StdPair { "cos"   , std::cos   },
                StdPair { "tan"   , std::tan    }, StdPair { "asin"  , std::asin   }, StdPair { "acos"  , std::acos  },
                StdPair { "atan"  , std::atan   }, StdPair { "sinh"  , std::sinh   }, StdPair { "cosh"  , std::cosh  },
                StdPair { "tanh"  , std::tanh   }, StdPair { "asing" , std::asinh  }, StdPair { "acosh" , std::acosh },
                StdPair { "atanh" , std::atanh  }, StdPair { "erf"   , std::erf    }, StdPair { "erfc"  , std::erfc  },
                StdPair { "tgamma", std::tgamma }, StdPair { "lgamma", std::lgamma }, StdPair { "ceil"  , std::ceil  },
                StdPair { "floor" , std::floor  }, StdPair { "trunc" , std::trunc  }, StdPair { "round" , std::round },
            };
            
            auto id = std::stol( expr[2] );
            
            for( auto [name, ptr] : stdfunctions )
            {
                if( expr[1] == name ) return UnaryOp { id, ptr };
            }

            if( expr[1] == "sign"   ) return UnaryOp { id, []( double x ) noexcept { return x >= 0.0 ? 1.0 : 0.0; } };
            if( expr[1] == "UAdd"   ) return UnaryOp { id, []( double x ) noexcept { return +x; } };
            if( expr[1] == "USub"   ) return UnaryOp { id, []( double x ) noexcept { return -x; } };
            if( expr[1] == "Not"    ) return UnaryOp { id, []( double x ) noexcept { return x == 0.0; } };
            if( expr[1] == "Invert" ) return UnaryOp { id, []( double x ) noexcept { return x - 1.0; } };
        }

        return std::nullopt;
    }
};

struct BinaryOp
{
    long left, right;
    std::function<double(double, double)> op;

    static std::optional<BinaryOp> create( const std::vector<std::string>& expr, size_t )
    {
        if( ( expr[0] == "BinOp" || expr[0] == "Call" || expr[0] == "Compare" || expr[0] == "BoolOp" ) && expr.size( ) == 4 )
        {
            using StdPair = std::pair<const char*, double(*)(double, double)>;
            using CustomPair = std::pair<const char*, decltype( op )>;

            auto stdfunctions = std::array
            {
                StdPair { "pow" , std::pow }, StdPair { "Pow" , std::pow }, StdPair { "hypot" , std::hypot }, 
                StdPair { "atan2" , std::atan2 }, StdPair { "mod" , std::fmod }, StdPair { "remainder" , std::remainder },
            };
                      
            auto customfunctions = std::array 
            {
                CustomPair { "Add",   []( double l, double r ) noexcept { return l + r; } },
                CustomPair { "Sub",   []( double l, double r ) noexcept { return l - r; } },
                CustomPair { "Mult",  []( double l, double r ) noexcept { return l * r; } },
                CustomPair { "Div",   []( double l, double r ) noexcept { return l / r; } },
                CustomPair { "Eq",    []( double l, double r ) noexcept { return l == r; } },
                CustomPair { "NotEq", []( double l, double r ) noexcept { return l != r; } },
                CustomPair { "Lt",    []( double l, double r ) noexcept { return l < r; } },
                CustomPair { "LtE",   []( double l, double r ) noexcept { return l <= r; } },
                CustomPair { "Gt",    []( double l, double r ) noexcept { return l > r; } },
                CustomPair { "GtE",   []( double l, double r ) noexcept { return l >= r; } },
                CustomPair { "And",   []( double l, double r ) noexcept { return l && r; } },
                CustomPair { "Or",    []( double l, double r ) noexcept { return l || r; } },
                CustomPair { "Mod",   []( double l, double r ) noexcept { return std::fmod( l, r ); } },
                CustomPair { "max",   []( double l, double r ) { return std::max( l, r ); } },
                CustomPair { "min",   []( double l, double r ) { return std::min( l, r ); } }
            };
  
            auto id1 = std::stol( expr[2] );
            auto id2 = std::stol( expr[3] );
                        
            for( auto [name, ptr] : stdfunctions )
            {
                if( expr[1] == name ) return BinaryOp { id1, id2, ptr };
            }   

            for( auto [name, fn] : customfunctions )
            {
                if( expr[1] == name ) return BinaryOp { id1, id2, fn };
            }
        }

        return std::nullopt;
    }
};

struct Op3
{
    std::array<long, 3> ids;
    std::function<double(double, double, double)> op;

    static std::optional<Op3> create( const std::vector<std::string>& expr, size_t )
    {
        if( ( expr[0] == "Op3" || expr[0] == "Call" ) && expr.size( ) == 5 )
        {
            using StdPair = std::pair<const char*, double(*)(double, double, double)>;
            using CustomPair = std::pair<const char*, decltype( op )>;

            auto stdfunctions = std::array
            {
                StdPair { "lerp" , std::lerp }
            };
                      
            auto customfunctions = std::array 
            {
                CustomPair { "select",   []( double cond, double v1, double v2 ) noexcept { return cond > 0.0 ? v1 : v2; } },
            };
  
            auto ids = std::array { std::stol( expr[2] ), std::stol( expr[3] ), std::stol( expr[4] ) };
                        
            for( auto [name, ptr] : stdfunctions )
            {
                if( expr[1] == name ) return Op3 { ids, ptr };
            }   

            for( auto [name, fn] : customfunctions )
            {
                if( expr[1] == name ) return Op3 { ids, fn };
            }
        }

        return std::nullopt;
    }
};

using Expression = std::variant<Constant, Input, UnaryOp, BinaryOp, Op3>;

// Parse input
Expression create( const std::vector<std::string>& expression, size_t ndim )
{
    MLHP_CHECK( !expression.empty( ), "Empty expression." );

    // Iterate over variant types
    auto iterate = [&]<size_t I = 0>( auto&& self ) -> Expression
    {
        // If index is within variant size
        if constexpr( I < std::variant_size_v<Expression> )
        {
            // Call create and return if successful, otherwise move to next index
            if( auto result = std::variant_alternative_t<I, Expression>::create( expression, ndim ); result )
            {
                return *result;
            }

            return self.template operator()<I + 1>( self );
        }

        auto message = std::string { "Unknown expression [" };

        for( auto& subexpr : expression )
        {
            message += "\"" + subexpr + "\", ";
        }

        message.erase( message.end( ) - 2, message.end( ) );

        MLHP_THROW( message + "]." );
    };

    return iterate( iterate );
}

// Dispatch during runtime using overload resolution
template<size_t D>
struct DispatchExpression 
{
    double call( long index ) const { return std::visit( *this, tree[static_cast<size_t>( index )] ); };

    double operator()( const Constant& node ) const noexcept { return node.value; }    
    double operator()( const Input& node ) const noexcept { return xyz[node.index]; }    
    double operator()( const UnaryOp& node ) const noexcept { return node.op( call( node.index ) ); }    
    double operator()( const BinaryOp& node ) const noexcept { return node.op( call( node.left ), call( node.right ) ); }
    double operator()( const Op3& node ) const noexcept { return node.op( call( node.ids[0] ), call( node.ids[1] ), call( node.ids[2] ) ); }

    const std::vector<Expression>& tree;
    const std::array<double, D>& xyz;
};

} // parser

template<size_t D>
void defineTreeParser( pybind11::module& m )
{
    m.def( add<D>( "internalSpatialFunctionFromAST" ).c_str( ), []( std::vector<std::vector<std::string>> ast )
    { 
        MLHP_CHECK( !ast.empty( ), "Empty tree." );

        auto nodes = std::vector<parser::Expression> { };

        for( auto& node : ast )
        {
            nodes.push_back( parser::create( node, D ) );
        }

        auto impl = [nodes = std::move( nodes )]( std::array<double, D> xyz )
        {
            return parser::DispatchExpression<D> { nodes, xyz }.call( 0 );
        };

        return ScalarFunctionWrapper<D> { std::move( impl ) };
    } );
}

template<size_t... D>
void bindParserDimensions( pybind11::module& m )
{
    [[maybe_unused]] std::initializer_list<int> tmp { ( defineTreeParser<D>( m ), 0 )... };
}

void bindParser( pybind11::module& m )
{
    bindParserDimensions<MLHP_DIMENSIONS_LIST>( m );
}

} // mlhp::bindings
