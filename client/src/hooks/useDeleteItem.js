import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { deleteItem } from '../api/apiItem'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';


export default function useDeleteCategory(item) {   
    const {user, setAlert} = useContext(AppContext)
    const navigate = useNavigate()


    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const deleteCat=async()=>{
                response = await deleteItem(user.token, item.id, source.token);
                if (response){
                    setAlert({msg:`Item: ${item.name} Deleted`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    ///redirect to the login page
                    navigate('/')

                }
            }
            if(item?.name){
                deleteCat();
            };
            return ()=>{source.cancel()}
        },[item, setAlert, user.token, navigate]
    )
  
}
