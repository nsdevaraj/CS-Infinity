
```js
import React, {useState} from 'react'
import ReactDOM from 'react-dom'

const CheckBox = ({isSelected, setIsSelected}) => {
  const value = isSelected ? 'X' : '0'
  // return <div onClick={setIsSelected}>{value}</div>

  return <CheckBox value={isSelected} onChange={setIsSelected} />
}

const getIntialAarray = () => {
  const returnAry = []

  for (let i = 0; i < 5; i++) {
    returnAry.push(false)
  }

  return returnAry
}

function App() {
  const [items, setItems] = useState(getIntialAarray())

  const setItem = (index) => {
    const newItems = items.slice()
    newItems[index] = !newItems[index]
    setItems(newItems)
  }

  const moveForward = () => {
    const newItems = items.slice()
    const lastItem = newItems.pop()

    setItems([lastItem, ...newItems])
  }

  const moveBackward = () => {
    const firstItem = items[0]
    setItems([...items.slice(1), firstItem])
  }

  return (
    <div>
      <div onClick={moveBackward}>Backward</div>

      {items.map((item, index) => (
        <CheckBox isSelected={item} setIsSelected={() => setItem(index)} />
      ))}
      <div onClick={moveForward}>Forward</div>
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById('root'))

```