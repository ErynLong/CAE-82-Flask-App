import apiClient from './clientTokenAuth'

const endpoint='/api/create-checkout-session'

export const postTransaction = async (token, data, cancelToken)=>{
    const response = await apiClient(token, cancelToken).post(endpoint, data);
    console.log('hereeeeeee',response)
    return window.location.href=response.data.url
}