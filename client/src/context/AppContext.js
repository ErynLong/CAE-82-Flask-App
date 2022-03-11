import {createContext, useState, useReducer, useEffect} from "react";
import {shopReducer, cartActions} from "../reducers/shopReducer";

export const AppContext = createContext();

const AppContextProvider = ({children})=>{

    const getUserFromLS=()=>{
        let user = localStorage.getItem('user');
        if(user){
            return JSON.parse(user)
        }
    }

    const getCartFromLS=()=>{
        let cart = localStorage.getItem('cart');
        if(cart){
            return JSON.parse(cart)
        }
        return []
    }



    const [user, _setUser]=useState(getUserFromLS());
    const [alert, setAlert]=useState({});
    const [cart, dispatch] = useReducer(shopReducer,getCartFromLS())

    useEffect(
        ()=>{
            localStorage.setItem('cart', JSON.stringify(cart))
        },
        [cart]
    )

    const values={
        user,
        setUser:(user)=>{
            localStorage.setItem('user',JSON.stringify(user))
            _setUser(user)
        },
        alert,
        setAlert,
        cart,
        addToCart:(item)=>{
            dispatch({type: cartActions.addToCart, item})
        },
        addBulkToCart:(item)=>{
            dispatch({type: cartActions.addBulkToCart, item})
        },
        removeFromCart:(item)=>{
            dispatch({type: cartActions.removeFromCart, item})
        },
        emptyCart:()=>{
            dispatch({type:cartActions.emptyCart})
        },
        removeAllFromCart:(item)=>{
            dispatch({type: cartActions.removeAllFromCart, item})
        }
    }

    return (
        <AppContext.Provider value={values}>
            {children}
        </AppContext.Provider>
    )

}

export default AppContextProvider