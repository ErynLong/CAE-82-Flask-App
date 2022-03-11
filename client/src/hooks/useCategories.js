
import {useEffect, useState} from 'react'
import {getCategories} from '../api/apiCategory';
import {CancelToken} from 'apisauce'

export default function useCategories() {
  const [categories, setCategories] = useState([])
  
  useEffect(
      ()=>{
          const source = CancelToken.source();
          const getCats=async()=>{
              const response = await getCategories(source.token)
              setCategories(response)
          }
          getCats()
          return ()=>{source.cancel();}
      },
      []
  )

  return categories
}
