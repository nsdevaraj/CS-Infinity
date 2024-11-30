import { render } from "solid-js/web";
import { createSignal } from "solid-js";

function Counter() {

  // signal 
  let [count, setCount] = createSignal(1);
  
  // function updates signal
  const increment = () => {
    // update by setter
    setCount(count => count + 1);
  }


  return (
    <button type="button" onClick={increment}>
      {
        // show count by observing count
        count()
        }
    </button>
  );
}

render(() => <Counter />, document.getElementById("app")!);
