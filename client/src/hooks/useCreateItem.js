import { useEffect, useContext } from 'react'
import { CancelToken } from 'apisauce'
import { postItem } from '../api/apiItem'
import { AppContext } from '../context/AppContext'
import { useNavigate } from 'react-router-dom';


export default function useCreateItem(item) {   
    const {user, setAlert} =useContext(AppContext)
        const navigate = useNavigate()


    useEffect(
        ()=>{
            let response
            const source = CancelToken.source()
            const createItem=async()=>{
                response = await postItem(user.token, item, source.token);
                if (response){
                    setAlert({msg:`Item: ${item.name} Created`, cat:'success'})
                }else if(response!==undefined && response ===false){
                    setAlert({msg:`Please Reauthorize Your Account`, cat:'warning'})
                    ///redirect to the login page
                    navigate('/')

                }
            }
            if(item?.name){
                createItem();
            };
            return ()=>{source.cancel()}
        },[item,setAlert, user.token, navigate]
    )
  
}
