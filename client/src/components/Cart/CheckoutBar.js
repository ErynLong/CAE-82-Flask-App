import {Typography, Box, Stack } from '@mui/material'
import { AppContext } from '../../context/AppContext'
import {useContext} from 'react'
import Button from '../Button'
import { useNavigate } from 'react-router-dom'
import CheckoutButton from '../CheckoutButton'

export default function CheckoutBar() {
    const {user, cart}=useContext(AppContext)
    const navigate = useNavigate()
    
    const handleLogin=()=>{navigate('/login')}

  return (
    <Box sx={{position: 'fixed', right:'10px', bottom:"10px", p:2, display:"flex", alignContent:"center", backgroundColor:"#33333325", border:'1px solid black' }}>
        <Stack>
            <Typography variant="h6">
                Cart Total : ${cart.reduce((total,nextItem)=>({"price":total.price+nextItem.price})).price.toFixed(2)}
            </Typography>
            {user?<CheckoutButton/>:<Button onClick={()=>{handleLogin()}}>Login to Pay</Button>}
        </Stack>

    </Box>
  )
}
