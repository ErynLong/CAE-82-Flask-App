import {useContext} from 'react';
import CartItem from './CartItem';
import { AppContext } from '../../context/AppContext';
import Box from '@mui/material/Box';
import CheckoutBar from './CheckoutBar';

export default function Cart() {
  const {cart} = useContext(AppContext)

  return (
    <>
    <Box sx={{mb:15}}>
    {
      [...new Set(cart.map(JSON.stringify))]
        .map(JSON.parse)?.map((item)=><CartItem key={item.id} item={item}/>)
    }
    </Box>
    <CheckoutBar/>
    </>
  )
}
