import React from 'react';
import { useState } from 'react';
import YouTube from 'react-youtube';

const Videos = () => {

  const [source,Setsource]=useState("PUB0TaZ7bhA");
  // Adding a variety of topics and more videos
  const videos = [
    { link: 'PUB0TaZ7bhA', title: 'Trigonometry Basics' },
    { link: '302eJ3TzJQU', title: 'Geometry Basics' },
    { link: 'NybHckSEQBI', title: 'Algebra Basics' },
    { link: 'WsQQvHm4lSw', title: 'Calculus Basics' },
    { link: 'kjBOesZCoqc', title: 'Linear Algebra' },
    { link: 'p_di4Zn4wz4', title: 'Differential Equations' },
    { link: 'zOjov-2OZ0E', title: 'Introduction to Programming' },
    { link: 'oz9cEqFynHU', title: 'Data Structures for Beginners' },
  ];

  return (
    <div className='relative flex p-4'>
      <h1 className='absolute -bottom-5 right-10'>Resources</h1>
      <YouTube 
              videoId={source}
              opts={{
                width: '100%',
                height: '100%',
                playerVars: {
                  autoplay: 0, // Don't autoplay
                  controls: 1, // Show controls
                  modestbranding: 1, // Reduce branding
                  rel: 0, // Don't show related videos
                }
              }} 
              className="rounded-lg w-2/3"
            />
            <div className='w-1/3'>
              <ul className='flex w-full flex-col p-0 justify-center bg-green-400'>
              {
                videos.map((e,i)=>(
                  <li onClick={()=>Setsource(e.link)} className={`text-center w-full rounded-lg hover:bg-green-300 ${source===e.link? "bg-green-300" :"bg-green-400"} cursor-pointer p-3`} key={i}>{e.title}</li>
                ))
              }
              </ul>
            </div>
    </div>
  );
};

export default Videos;
