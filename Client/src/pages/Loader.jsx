import React from 'react'
import { TailSpin } from 'react-loader-spinner'

const Loader = () => {
  return (
        <TailSpin
  visible={true}
  height="full"
  width="full"
  color="rgb(59,149,248)"
  ariaLabel="tail-spin-loading"
  radius="1"
  wrapperStyle={{}}
  wrapperClass=""
  />      
  )
}

export default Loader