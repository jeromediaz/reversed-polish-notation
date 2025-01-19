import './App.css';
import Calculator from './Calculator/Calculator'
import {ReactComponent as CSVIcon} from './csv-file.svg'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        Simple Reversed Polish Notation calculator
      </header>
      <main>
        <Calculator />
        <div className="App-export">
          <a href="http://localhost:8000/calculations"><CSVIcon height={24} width={24}/></a>
        </div>
      </main>
    </div>
  );
}

export default App;
