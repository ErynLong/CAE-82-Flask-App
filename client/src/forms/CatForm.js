import React, {useState} from 'react'
import * as Yup from "yup";
import { useFormik } from 'formik';
import Button from '../components/Button';
import TextField from '@mui/material/TextField';
import useCreateCategory from '../hooks/useCreateCategory';
import useEditCategory from '../hooks/useEditCategory';
import useDeleteCategory from '../hooks/useDeleteCategory';

const FormSchema =Yup.object(
   { 
       "name":Yup.string().required("Required")
    }
)


// {id:1, name:"Pants"}
export default function CatForm({ category }) {

    const [newCat, setNewCat] = useState({})
    const [editCat, setEditCat] = useState({})
    const [deleteCat, setDeleteCat] = useState({})

    useCreateCategory(newCat)
    useEditCategory(editCat)
    useDeleteCategory(deleteCat)
    const initialValues ={
        name:category?.name ?? ''
    };

    const handleSubmit =(values, resetForm)=>{
        if (!category){
            setNewCat(values)
        }else{
            setEditCat({...values, id:category.id})
        }
        console.log(values)
        resetForm(initialValues);
    }

    const formik = useFormik({
        initialValues:initialValues,
        validationSchema:FormSchema,
        onSubmit:(values, {resetForm})=>{handleSubmit(values, resetForm)},
        enableReinitialize:true

    })
    
    const handleDelete=()=>{
        setDeleteCat(category)
    }

  return (
    <form onSubmit={formik.handleSubmit}>
        <TextField
            fullWidth
            id="name"
            name="name"
            type="text"
            sx={{mb:2, mt:2}}
            label="Name"
            placeholder="name"
            value={formik.values.name}
            onChange={formik.handleChange}
            error={formik.touched.name && Boolean(formik.errors.name)}
            helperText={formik.touched.name && formik.errors.name}        
        />
        <Button type="submit" sx={{width:"100%", my:1}}>{category?'Edit Category':'Create Category'}</Button>
        <Button color="error" onClick={()=>handleDelete()} sx={{width:"100%", my:1}}>Delete Category</Button>
    </form>
  )
}
