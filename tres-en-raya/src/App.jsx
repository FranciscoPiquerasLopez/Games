import { useState, useEffect } from 'react'
import confetti from 'canvas-confetti'
import './App.css'

function Square({ children, index, updateBoard, isSelected }) {

  const classNameTurnSelected = isSelected ? 'is-selectedCell' : 'cell'

  const handleClick = () => {
    updateBoard(index)
  }

  return (
    <div onClick={handleClick} className={classNameTurnSelected}>
      {children}
    </div>
  )
}

function App() {

  // CONSTANTES
  const VALUES = {
    X: '❌',
    O: '⚪'
  }

  const COMBOS_WINNER = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]

  // ESTADOS Y HOOKS
  const [board, setBoard] = useState(() => {
    const getBoardFromStorage = localStorage.getItem('board')
    if (getBoardFromStorage) return JSON.parse(getBoardFromStorage)
    return Array(9).fill(null)
  })

  const [turn, setTurn] = useState(() => {
    const getTurnFromStorage = localStorage.getItem('turn')
    // Los ?? lo que hacen es devolver el valor predeterminado en caso de que sea null o vacío
    return getTurnFromStorage ?? VALUES.X
  })
  const [winner, setWinner] = useState(null)

  // Guardar el estado en localStorage cada vez que cambie el turno o el tablero
  useEffect(() => {
    saveGameToStorage()
  }, [turn, board])

  // Función para guardar la partida en el localStorage
  const saveGameToStorage = () => {
    localStorage.setItem('turn', turn);
    localStorage.setItem('board', JSON.stringify(board));
  }

  // FUNCIONES
  const resetGame = () => {
    setTurn(VALUES.X)
    setBoard(Array(9).fill(null))
    setWinner(null)

    // Eliminarlo tamibén del localStorage
    localStorage.removeItem('turn')
    localStorage.removeItem('board')
  }

  const checkWinner = (newBoard) => {
    for (const row of COMBOS_WINNER) {
      const [a, b, c] = row

      if (newBoard[a] != null && newBoard[b] != null && newBoard[c] != null) {
        if (newBoard[a] === newBoard[b] && newBoard[a] === newBoard[c]) return newBoard[a]
      }

      if (newBoard.every(cell => cell !== null)) {
        return false
      }
    }
    return null
  }

  const updateBoard = (index) => {
    // Comprobamos que no se sobreescriban las celdas
    if (board[index] || winner) return

    // Establecemos el turno
    const newTurn = VALUES.X === turn ? VALUES.O : VALUES.X
    setTurn(newTurn)

    const newBoard = [...board]
    newBoard[index] = turn
    setBoard(newBoard)

    // Comprobamos el ganador
    const newWinner = checkWinner(newBoard)

    if (newWinner != null) {
      if (newWinner != false) {
        // Lanzar confetti
        confetti()
      }
      setWinner(newWinner)
    }
  }

  return (
    <>
      <h1>Tres en raya</h1>
      <button onClick={resetGame}>Empezar de nuevo</button>
      <div className='board-container'>
        {
          board.map((_, index) => (
            <Square
              key={index}
              index={index}
              updateBoard={updateBoard}
            >
              {board[index]}
            </Square>
          ))
        }
      </div>

      <div className='turn'>
        <Square isSelected={turn === VALUES.X}>
          {VALUES.X}
        </Square>

        <Square isSelected={turn === VALUES.O}>
          {VALUES.O}
        </Square>
      </div>

      {
        winner != null && (
          <section className='winner'>
            <div className='text'>
              <h2>
                {
                  winner != false
                    ? 'Ganó:'
                    : 'Empate'
                }
              </h2>

              <header className='win'>
                {winner != false && <Square>{winner}</Square>}
              </header>

              <footer>
                <button onClick={resetGame}>
                  Empezar de nuevo
                </button>
              </footer>
            </div>
          </section>
        )
      }
    </>
  )
}

export default App
