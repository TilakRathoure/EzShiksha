import React from 'react';
import YouTube from 'react-youtube';

const Videos = () => {
  // Adding a variety of topics and more videos
  const videos = [
    { link: 'OIJdbwCBZHc', title: 'Trigonometry Basics' },
    { link: 'vFvxeDrjmxA', title: 'Geometry Basics' },
    { link: 'fpz9XzT9lIo', title: 'Algebra Basics' },
    { link: 'XkYwVUG1awI', title: 'Calculus Basics' },
    { link: 'tVCzXrlB0b4', title: 'Linear Algebra' },
    { link: 'i61lH4yNJnM', title: 'Differential Equations' },
    { link: 'ZjVeZ1KL6bc', title: 'Introduction to Programming' },
    { link: 'eAoZZj_rqp4', title: 'Data Structures for Beginners' },
  ];

  return (
    <div className="min-h-screen flex flex-wrap items-center justify-center gap-6 p-8 bg-gradient-to-r from-blue-100 to-purple-300">
      {videos.map((video, index) => (
        <div key={index} className="max-w-xs w-full bg-white shadow-lg rounded-lg overflow-hidden flex flex-col items-center justify-between h-full">
          <h5 className="text-center text-xl font-semibold mb-3 text-blue-600">{video.title}</h5>
          <div className="flex-1 w-full h-full">
            <YouTube 
              videoId={video.link}
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
              className="rounded-lg"
            />
          </div>
        </div>
      ))}
    </div>
  );
};

export default Videos;
