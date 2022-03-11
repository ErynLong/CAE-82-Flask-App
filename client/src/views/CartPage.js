import React, {useContext, useEffect} from 'react'
import {AppContext} from '../context/AppContext'
import Cart from '../components/Cart/Index'
import Typography from '@mui/material/Typography';
import {useParams} from 'react-router-dom';
export default function CartPage() {
    
    const {cart,setAlert} = useContext(AppContext)
    const {canceled} = useParams()
    useEffect(
      ()=>{
        if(canceled){
          setAlert({msg:'Checkout Canceled',cat:'error'})
        }
      }
      ,[canceled,setAlert]
    )

    if (cart.length<=0){
        return(
      <Typography variant='h3'>Your Cart is Empty</Typography>
        )
    }
  return (
    <>    
        <Typography variant='h3'>Your Cart</Typography>
        <Cart/>
    </>

  )
}
