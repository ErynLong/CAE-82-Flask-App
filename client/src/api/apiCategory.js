import  apiClientNoAuth from './clientNoAuth'
import apiClientTokenAuth from './clientTokenAuth'

const endpoint = '/api/category'

export const getCategories = async (cancelToken) =>{
    let error;
    let categories;

    const response = await apiClientNoAuth(cancelToken).get(endpoint);
    if (response.ok){
        categories=response.data.categories
    }else{
        error = 'An Unexpected Error has Occured. Please Try Again'
    }

    return{
        error,
        categories,
    }
}

export const postCategory = async(token, catName, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).post(endpoint,{name:catName});
    return response.ok
}


export const putCategory = async(token,id, catName, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).put(endpoint+'/'+id,{name:catName});
    return response.ok
}


export const deleteCategory = async(token, id, cancelToken)=>{
    const response = await apiClientTokenAuth(token,cancelToken).delete(endpoint+'/'+id);
    return response.ok
}
