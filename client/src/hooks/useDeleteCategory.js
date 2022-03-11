import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { deleteCategory } from '../api/apiCategory'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';


export default function useDeleteCategory(category) {   
    const {user, setAlert} = useContext(AppContext)
        const navigate = useNavigate()


    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const deleteCat=async()=>{
                response = await deleteCategory(user.token, category.id, source.token);
                if (response){
                    setAlert({msg:`Category: ${category.name} Deleted`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    //redirect to the login page
                                        navigate('/')

                }
            }
            if(category?.name){
                deleteCat();
            };
            return ()=>{source.cancel()}
        },[category, setAlert, user.token, navigate]
    )
  
}
