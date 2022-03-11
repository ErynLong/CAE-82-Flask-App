
import { CancelToken } from 'apisauce';
import {useEffect, useState} from 'react'
import {getItem} from '../api/apiItem'

export default function useSingleItem(itemId) {
    const[item, setItem] = useState([])

    useEffect(
        ()=>{
            let source;
            (async()=>{
                source = CancelToken.source()
                const response = await getItem(itemId, source.token)
                setItem(response)
            })()
            return ()=>{source.cancel()}
        },[itemId]
    )

  return item
}
