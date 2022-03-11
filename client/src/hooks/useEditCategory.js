import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { putCategory } from '../api/apiCategory'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';


export default function useEditCategory(category) {   
    const {user, setAlert} =useContext(AppContext)
        const navigate = useNavigate()


    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const editCat=async()=>{
                response = await putCategory(user.token, category.id, source.token);
                if (response){
                    setAlert({msg:`Category: ${category.name} Edited`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    ///redirect to the login page
                    navigate('/')

                }
            }
            if(category?.name){
                editCat();
            };
            return ()=>{source.cancel()}
        },[category, setAlert,user.token, navigate]
    )
  
}
