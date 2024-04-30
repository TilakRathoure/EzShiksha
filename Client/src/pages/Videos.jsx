import React from 'react';
import YouTube from 'react-youtube';

const Videos = () => {
  const videos = [
    { link: 'OIJdbwCBZHc&t=3s', title: "Trignometry Basics" },
    { link: 'OIJdbwCBZHc&t=3s', title: "Geometry basics" },
    { link: 'OIJdbwCBZHc&t=3s', title: "Algebra Basics" },
    { link: 'OIJdbwCBZHc&t=3s', title: "Calculus Basics" },
  ];

  return (
    <div className='flex flex-wrap items-center justify-center gap-5 p-4 pt-5 bg-gradient-to-r from-blue-100'>
      {videos.map((video, index) => (
        <div key={index}>
          <h5 className='w-full text-center mb-3'>{video.title}</h5>
          <YouTube videoId={video.link} className='' opts={{
            width: '560',
            height: '315',
            playerVars: {}
          }} />
        </div>
      ))}
    </div>
  );
};

export default Videos;
