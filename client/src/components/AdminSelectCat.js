import React, { useState } from 'react'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import CatForm from '../forms/CatForm';
import Typography from '@mui/material/Typography';
import useCategories from '../hooks/useCategories';
import Error from '../components/Error';

export default function AdminSelectCat() {
    const [cat, setCat] = useState('');
    const {categories, error} = useCategories();


    const handleChange = (event) => {
        console.log(event.target.value)
        if(event.target.value === "default"){
            setCat("")
            return
        }
        setCat(JSON.parse(event.target.value));
    };
  
  return (
      <>
        <FormControl fullWidth>
            <InputLabel id="category-label">Category</InputLabel>
            <Select
                labelId="category-label"            
                label="Category"
                name="category_id"
                value={cat?JSON.stringify(cat):'default'}
                placeholder="category"
                onChange={(event)=>handleChange(event)}
            >
                <MenuItem value="default"><em>Select Category to Edit</em></MenuItem>
                {categories?.map(
                    (category)=>(
                        <MenuItem key={category.id}  value={JSON.stringify(category)}>{category.name} | {category.id}</MenuItem>
                    )
                )}
                
            </Select>
            <Error>{error}</Error>
        </FormControl>
    
        {cat ?
        <>
            <Typography sx={{p:4}} variant="h5">
                Edit {cat.name}
            </Typography>
            <CatForm category={cat}/>
        </>
            :
        <>
            <Typography sx={{p:4}} variant="h5">
                Create Category
            </Typography>
            <CatForm/>
        </>
        }
        </>  
  )
}
