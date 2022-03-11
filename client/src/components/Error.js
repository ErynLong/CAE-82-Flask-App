import React from 'react'

export default function Error({style, children, ...props}) {
    const styles={
        error:{
            color:"red"
        }

    }

  return (
    <div style={{...styles.error, ...style}} {...props} >
        {children}
    </div>
  )
}
