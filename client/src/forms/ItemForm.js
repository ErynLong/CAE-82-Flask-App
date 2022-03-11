import React from 'react'
import * as Yup from "yup";
import { useFormik } from 'formik';
import Button from "../components/Button";
import { useState } from 'react';
import TextField from '@mui/material/TextField';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import FormHelperText from '@mui/material/FormHelperText';
import useCategories from '../hooks/useCategories';
import useCreateItem from '../hooks/useCreateItem';
import useEditItem from '../hooks/useEditItem';
import useDeleteItem from '../hooks/useDeleteItem';


const FormSchema = Yup.object({
    "name":Yup.string().required("Required"),
    "desc":Yup.string().required("Required"),
    "price":Yup.string().matches(/^\d+(\.\d{1,2})?$/, "Must be a Valid Price").required("Required"),
    "img":Yup.string().required("Required"),
    "category_id":Yup.number().integer().required("Required")
})

// {id:1, name:"item1", desc:'my test item', category_id:3, price: 9.99, img:'my-image.png'}
export default function ItemForm({item}) {
    const {categories, catError} = useCategories();

    const [newItem, setNewItem] = useState({})
    const [editItem, setEditItem] = useState({})
    const [deleteItem, setDeleteItem] = useState({})


    useCreateItem(newItem)
    useEditItem(editItem)
    useDeleteItem(deleteItem)

    const initialValues={
        name:item?.name ?? '',
        desc:item?.desc ?? '',
        price:item?.price ?? '',
        img:item?.img ?? '',
        category_id:item?.category_id ?? ''
    }

    const handleSubmit =(values,resetForm)=>{
        console.log(values)
        if(!item){
            setNewItem(values)
        }else{
            setEditItem({...values, id:item.id})
        }
        resetForm(initialValues);
    }

    const formik = useFormik({
        initialValues:initialValues,
        validationSchema:FormSchema,
        onSubmit:(values, {resetForm})=>{handleSubmit(values, resetForm)},
        enableReinitialize:true

    })
        
    const handleDelete=()=>{
        setDeleteItem(item)
    }

  return (
    <form onSubmit={formik.handleSubmit}>
    <TextField
        fullWidth
        id="name"
        name="name"
        type="text"
        sx={{ mb: 2, mt: 2 }}
        label="Name"
        placeholder="My New Item"
        value={formik.values.name}
        onChange={formik.handleChange}
        error={formik.touched.name && Boolean(formik.errors.name)}
        helperText={formik.touched.name && formik.errors.name}
    />
    <TextField
        fullWidth
        id="desc"
        name="desc"
        sx={{mb: 2 }}
        type="text"
        label="Description"
        placeholder="This item is amazing"
        value={formik.values.desc}
        onChange={formik.handleChange}
        error={formik.touched.desc && Boolean(formik.errors.desc)}
        helperText={formik.touched.desc && formik.errors.desc}
    />
    <TextField
        fullWidth
        id="price"
        name="price"
        sx={{ mb: 2 }}
        type="number"
        label="Price"
        placeholder="9.99"
        value={formik.values.price}
        onChange={formik.handleChange}
        error={formik.touched.price && Boolean(formik.errors.price)}
        helperText={formik.touched.price && formik.errors.price}
    />
    <TextField
        fullWidth
        id="img"
        name="img"
        sx={{ mb: 2 }}
        type="text"
        label="Image URL"
        placeholder="http://www.mycms.com/image.png"
        value={formik.values.img}
        onChange={formik.handleChange}
        error={formik.touched.img && Boolean(formik.errors.img)}
        helperText={formik.touched.img && formik.errors.img}
    />

<FormControl sx={{  width: "100%" }}>
    <InputLabel id="category-label-id">Category</InputLabel>
    <Select
        labelId="category-label-id"
        id="category-id"
        value={formik.values.category_id}
        name="category_id"
        label="Category"
        placeholder="category"
        onChange={formik.handleChange}
        error={formik.touched.category_id && Boolean(formik.errors.category_id)}
    >
        <MenuItem value=""><em>None</em></MenuItem>
        {categories?.map((category) => (
            <MenuItem key={category.id} value={category.id}>{category.name} | {category.id}</MenuItem>
        ))}
    </Select>
    {catError}
    <FormHelperText>{formik.touched.category_id && formik.errors.category_id}</FormHelperText>
</FormControl>

<Button type="submit" sx={{ width: "100%", my:1 }}>{item?'Submit Edit':'Create Item'}</Button>
<Button color="error" onClick={()=>handleDelete()} sx={{width:"100%", my:1}}>Delete Item</Button>

</form>
  )
}
