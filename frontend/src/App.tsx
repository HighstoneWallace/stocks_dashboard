import React, { useState } from 'react'
import Search from './components/Search.jsx'

const App = () => {

  const [searchTerm, setSearchTerm] = useState("")

  return (
    <main> 
      <div className = "pattern" />

      <div className = "wrapper">
        <header>
          <img src = "./logo.png" alt = "Logo" style={{ width: "100px", height: "100px" }}/>
          <h1>Track your <span className = "text-gradient">investments</span></h1>
        </header>
        <Search searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
      </div>

    </main>
  )
}

export default App