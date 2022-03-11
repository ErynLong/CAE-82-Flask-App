import  apiClientNoAuth from './clientNoAuth'
import apiClientTokenAuth from './clientTokenAuth'

const endpoint = '/api/item'

export const getItems = async (cancelToken) =>{
    let error;
    let items;

    const response = await apiClientNoAuth(cancelToken).get(endpoint);
    if (response.ok){
        items=response.data.items
    }else{
        error = 'An Unexpected Error has Occured. Please Try Again'
    }
    
    return{
        error,
        items,
    }
}

export const getItem = async (id, cancelToken) =>{
    let error;
    let item;
    const response = await apiClientNoAuth(cancelToken).get(endpoint+'/'+id);
    if (response.ok){
        item=response.data
    }else if (response.status === 404 ){
        error = 'Your item was not found'
    }
    else{
        error = 'An Unexpected Error has Occured. Please Try Again'
    }
    return{
        error,
        item,
    }
}

export const getItemsByCat = async(id, cancelToken)=>{
    let error;
    let items;

    const response = await apiClientNoAuth(cancelToken).get(endpoint+'/category/'+id);
    if (response.ok){
        items=response.data.items
    }else{
        error = 'An Unexpected Error has Occured. Please Try Again'
    }
    
    return{
        error,
        items,
    }
}


export const postItem = async(token, data, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).post(endpoint,data);
    return response.ok
}


export const putItem = async(token,id, data, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).put(endpoint+'/'+id,data);
    return response.ok
}


export const deleteItem = async(token, id, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).delete(endpoint+'/'+id);
    return response.ok
}
