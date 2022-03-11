import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { putItem } from '../api/apiItem'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';


export default function useEdititem(item) {   
    const {user, setAlert} =useContext(AppContext)
    const navigate = useNavigate()
 

    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const editItem=async()=>{
                response = await putItem(user.token, item.id, item, source.token);
                if (response){
                    setAlert({msg:`Item: ${item.name} Edited`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    ///redirect to the login page
                    navigate('/')
                }
            }
            if(item?.name){
                editItem();
            };
            return ()=>{source.cancel()}
        },[item, setAlert, user.token, navigate]
    )
  
}
