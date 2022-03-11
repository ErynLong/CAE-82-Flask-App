import React from 'react'
import Button from '@mui/material/Button';

export default function myButton({children, variant, ...props}) {
  return (
    <Button variant={variant??"contained"} {...props}>
        {children}
    </Button>
  )
}


