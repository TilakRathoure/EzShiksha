import React from 'react'
import formula from '../assests/images/calculating (1).png'
import note from '../assests/images/writing.png'
import para from '../assests/images/grammar.png'
import imag from '../assests/images/image.png'
import { Link } from 'react-router-dom'

const Divein = () => {
    const elements=[{name:"Solving Questions",img:formula, p:"Snap, solve. Math made easy. Revolutionize your learning!" ,ap:"/formula"},{name:"Note Making", img:note, p:"Upload image, get concise notes instantly. Simplify your studies!" ,ap:"/notemaking"},{name:"Paraphrasing and Spell Check", img:para, p:"Upload text or image, get paraphrased version instantly.", ap:"/paraphrase"},{name:"Extract text from Image", img:imag, p:"Upload image, get text extracted from it easily" , ap:"/extract"}]


  return (
    <div className='bg-gradient-to-r from-blue-100 w-[100vw] pb-8'>
        <container className="flex flex-wrap gap-5 px-3 items-center justify-center pt-12 w-full h-full">
            {elements.map((e)=>(
              
                <Link to={e.ap} className='no-underline'>
                <div className='bg-white w-[100%] h-[350px] flex flex-col items-center justify-center rounded-2xl shadow-2xl p-4 hover:scale-105 transition translate-y-2 cursor-pointer gap-3'><img src={e.img} className='w-[50%] h-[30%] object-contain ' alt="" /><h5 className=''>{e.name}</h5>
                <p className='text-black leading-6'>{e.p}</p></div></Link>
              ))}
        </container>
    </div>
  )
}

export default Divein