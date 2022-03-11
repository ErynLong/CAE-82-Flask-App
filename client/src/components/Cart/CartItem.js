import React, {useEffect, useState, useContext} from 'react'
import { styled } from '@mui/material/styles';
import Avatar from '@mui/material/Avatar';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import {useTheme} from '@mui/material/styles';
import CartCard from './CartCard';
import ChangeCartItemQuantity from './ChangeCartItemQuantity';
import { AppContext } from '../../context/AppContext';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? theme.palette.secondary : theme.palette.primary,
    ...theme.typography.body2,
    padding: theme.spacing(1),
    alignItems: 'center',
    justifyContent:'center',
    textAlign: 'center',
    display:'flex',
    color: theme.palette.text.secondary,
  }));
  
  export default function CartItem({item}) {
    const theme = useTheme();
    const {cart} = useContext(AppContext);
    
    const [qty,setQty]=useState(cart.filter((cartItem)=>cartItem.id === item.id).length)

    useEffect(
        ()=>{
            setQty(cart.filter((cartItem)=>cartItem.id === item.id).length)
        },[cart, item]
    )
    

  return (
    <Grid container spacing={2} sx={{m:1, pr:2, border: '1px solid', borderRadius:1, alignItems:"stretch"}}>
        <Grid item md={4} sm={6} xs={12}>
            {console.log(theme)}
            <Item sx={{height:'100%'}}>
                <Avatar alt={item.name} sx={{height:'100%', width:"100%"}} variant="rounded" src={item.img}/>
            </Item>
        </Grid>
        <Grid item md={3} sm={6} xs={12}>
            <Item sx={{height:'100%'}}>
                <CartCard item={item}/>
            </Item>
        </Grid>
        <Grid item md={2} sm={6} xs={12}>
            <Item sx={{height:'100%', alignContent:'center'}}>
                <ChangeCartItemQuantity item={item} qty={qty}/>
            </Item>
        </Grid>
        <Grid item md={3} sm={6} xs={12}>
            <Item sx={{height:'100%'}}>
                <div>
                <strong>Item Subtotal</strong>
                <br/>
                ${(item.price*qty).toFixed(2)}
                </div>

            </Item>
        </Grid>
        
    </Grid>
  )
}
