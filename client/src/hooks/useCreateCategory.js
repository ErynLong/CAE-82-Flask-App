import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { postCategory } from '../api/apiCategory'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';

export default function useCreateCategory(category) {   
    const {user, setAlert} =useContext(AppContext)
    const navigate = useNavigate()
    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const createCat=async()=>{
                response = await postCategory(user.token, category.name, source.token);
                if (response){
                    setAlert({msg:`Category: ${category.name} Created`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    navigate('/')
                }
            }
            if(category?.name){
                createCat();
            };
            return ()=>{source.cancel()}
        },[category,setAlert, user.token, navigate]
    )
  
}
