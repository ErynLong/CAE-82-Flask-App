
import { styled } from '@mui/material/styles';
import Avatar from '@mui/material/Avatar';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

import { Box, Typography } from '@mui/material';
import Error from './Error'
import CircularProgress from '@mui/material/CircularProgress';
import useSingleItem from '../hooks/useSingleItem';
import { useParams } from 'react-router-dom';

const Item = styled(Paper)(({ theme }) => ({
    backgroundColor: theme.palette.mode === 'dark' ? theme.palette.secondary : theme.palette.primary,
    ...theme.typography.body2,
    padding: theme.spacing(1),
    alignItems: 'center',
    justifyContent:'center',
    textAlign: 'center',
    color: theme.palette.text.secondary,
  }));
  
  export default function MyItem() {
    // get the query params
    const {itemId} = useParams();
    // use that to look up info on 1 item
    const {item, error}= useSingleItem(itemId);


    if(error){
        return(
        <Box sx={{display:"flex", width:'100%', height:"100%", alignItems:'center', justifyItems:'center', alignContent:'center', justifyContent:'center'}}>
            <Error>{error}</Error>
        </Box>)
    }
    if(!item){
    return(
        <Box sx={{display:"flex", width:'100%', height:"100%", alignItems:'center', justifyItems:'center', alignContent:'center', justifyContent:'center'}}>
            <CircularProgress/>
        </Box>)
    }
    

  return (
    <Grid container spacing={1} sx={{m:1, pr:2, border: '1px solid', borderRadius:1}}>
    
        <Grid item md={12} sm={12} xs={12}>
            <Item sx={{display:"flex"}}>
                <Avatar alt={item.name} sx={{height:'30%', width:'30%'}} variant="rounded" src={item?.img}/>
            </Item>
        </Grid>
        <Grid item md={12} sm={12} xs={12}>
            <Item sx={{height:'100%', alignContent:"center"}}>
                <Typography variant="subtitle1"><strong>Item name:</strong></Typography>
                <Typography variant="body1">{item.name}</Typography>
            </Item>
        </Grid>
        <Grid item md={6} sm={6} xs={6}>
            <Item sx={{height:'100%', alignContent:'center'}}>
            <Typography variant="subtitle1"><strong>Price:</strong></Typography>
                <Typography variant="body1">$ {item.price}</Typography>
            </Item>
        </Grid>
        <Grid item md={6} sm={6} xs={6}>
            <Item sx={{height:'100%'}}>
            <Typography variant="subtitle1"><strong>Item ID:</strong></Typography>
                <Typography variant="body1">{item.id}</Typography>
            </Item>
        </Grid>
        <Grid item md={12} sm={12} xs={12}>
            <Item sx={{height:'100%'}}>
            <Typography variant="subtitle1"><strong>Description:</strong></Typography>
                <Typography variant="body1">{item?.desc}</Typography>
            </Item>
        </Grid>
        <Grid item md={12} sm={12} xs={12}>
            <Item sx={{height:'100%'}}>
            <Typography variant="subtitle1"><strong>Category:</strong></Typography>
                <Typography variant="body1">{item?.category_name}</Typography>
            </Item>
        </Grid>
    </Grid>
  )
}
