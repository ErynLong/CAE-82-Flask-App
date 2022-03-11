import React, {useState} from 'react';
import Chip from '@mui/material/Chip';
import useCategories from '../hooks/useCategories';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import Error from './Error';
// const categories = [{id: 1, name:"Ditto"}, {id:2, name:"Pikachu"}, {id:3, name:"Mew"}]

export default function CategoryBar({handleClick=()=>{}}) {
    const [actCat, setActCat]= useState({});
    const {categories, error} = useCategories();
    
    const handleActCat=(cat)=>{
        if (actCat === cat){
            setActCat({})
        }else{
            setActCat(cat)
        }
    }
    
    if (error){
        return(
        <Box sx={{display:'flex'}}>
        <Error>{error}</Error>
        </Box>)
    }

    if (!categories){
        return(
        <Box sx={{display:'flex'}}>
            <CircularProgress />
        </Box>)
    }
  
  return (
  <>
    {categories?.map(
        (cat)=>(
            cat === actCat
            ?
            <Chip
            key={cat.id}
            label={cat.name}
            color="primary"
            size="small"
            sx={{mx:1}}
            onClick={()=>{handleActCat(cat); handleClick(cat);}}
            />
            :
            <Chip
            key={cat.id}
            label={cat.name}
            color="primary"
            variant="outlined"
            size="small"
            sx={{mx:1}}
            onClick={()=>{handleActCat(cat); handleClick(cat);}}
            />
        )
    )}
  </>
  )
}
