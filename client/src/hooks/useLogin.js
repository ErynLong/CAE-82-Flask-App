

import {useEffect} from 'react';
import {getUser} from  "../api/apiBasicAuth";
import { CancelToken } from 'apisauce';
import { useNavigate } from 'react-router-dom';


export default function useLogin(loginCreds, setError, setUser, setLoginCreds) {
        const navigate = useNavigate()

    useEffect(
        ()=>{
            const source = CancelToken.source()
            const login=async()=>{
                const response_object = await getUser(loginCreds.email, loginCreds.password, source.token)
                if (response_object.user?.token){
                    console.log('logged in');
                    setUser(response_object.user);
                    setError(response_object.error);
                    setLoginCreds({});
                    navigate('/')

                }
            };

            if (loginCreds.email && loginCreds.password){
                login();
            };
            return ()=>{
                source.cancel()
            }
        },
        [loginCreds, setLoginCreds, setUser, setError, navigate]
    )
}