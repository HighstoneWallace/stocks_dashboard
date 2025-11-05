import React from 'react'

const Search = ({searchTerm, setSearchTerm}) => {
  return (
    <div className = "search">
        <div>
            <img src = "search.svg" alt = "search" />
            <input
            type = "text"
            placeholder = "Enter the ticker symbol..."
            value = {searchTerm}
            onChange = {(event) => setSearchTerm(e.target.value.toUpperCase())}
            />
        </div>
    </div>
  )
}

export default Search