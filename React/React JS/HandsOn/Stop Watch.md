

If you don't clear the timeInterval, then it cause memory leaks


```jsx
import React, { useState, useRef, useEffect } from "react";

const Stopwatch = () => {
  const [time, setTime] = useState(0); // Time in milliseconds
  const [isRunning, setIsRunning] = useState(false);
  const timerRef = useRef(null);
  
  // Cleanup the interval on component unmount
  useEffect(() => {
    return () => {
      clearInterval(timerRef.current);
    };
  }, []);

  // Start the stopwatch
  const startStopwatch = () => {
    if (!isRunning) {
      setIsRunning(true);
      timerRef.current = setInterval(() => {
        setTime((prevTime) => prevTime + 10); // Increment time by 10ms
      }, 10);
    }
  };

  // Pause the stopwatch
  const pauseStopwatch = () => {
    setIsRunning(false);
    clearInterval(timerRef.current);
  };

  // Reset the stopwatch
  const resetStopwatch = () => {
    setIsRunning(false);
    clearInterval(timerRef.current);
    setTime(0);
  };

  // Format time (MM:SS:MS)
  const formatTime = () => {
    const minutes = Math.floor(time / 60000);
    const seconds = Math.floor((time % 60000) / 1000);
    const milliseconds = Math.floor((time % 1000) / 10);

    return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}:${String(milliseconds).padStart(2, "0")}`;
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Stopwatch</h1>
      <h2>{formatTime()}</h2>
      <div>
        {!isRunning ? (
          <button onClick={startStopwatch}>Start</button>
        ) : (
          <button onClick={pauseStopwatch}>Pause</button>
        )}
        <button onClick={resetStopwatch}>Reset</button>
      </div>
    </div>
  );
};

export default Stopwatch;

```



```jsx

import React, { useState, useEffect } from "react";

const Stopwatch = () => {
  const [time, setTime] = useState(0); // Time in milliseconds
  const [isRunning, setIsRunning] = useState(false);

  // useEffect to handle the interval when `isRunning` changes
  useEffect(() => {
    let timerId;

    if (isRunning) {
      timerId = setInterval(() => {
        setTime((prevTime) => prevTime + 10); // Increment time by 10ms
      }, 10);
    }

    // Cleanup function to clear the interval
    return () => clearInterval(timerId);
  }, [isRunning]);

  const startStopwatch = () => {
    setIsRunning(true);
  };

  const pauseStopwatch = () => {
    setIsRunning(false);
  };

  const resetStopwatch = () => {
    setIsRunning(false);
    setTime(0);
  };

  const formatTime = () => {
    const minutes = Math.floor(time / 60000);
    const seconds = Math.floor((time % 60000) / 1000);
    const milliseconds = Math.floor((time % 1000) / 10);

    return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}:${String(milliseconds).padStart(2, "0")}`;
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Stopwatch</h1>
      <h2>{formatTime()}</h2>
      <div>
        {!isRunning ? (
          <button onClick={startStopwatch}>Start</button>
        ) : (
          <button onClick={pauseStopwatch}>Pause</button>
        )}
        <button onClick={resetStopwatch}>Reset</button>
      </div>
    </div>
  );
};

export default Stopwatch;

```



