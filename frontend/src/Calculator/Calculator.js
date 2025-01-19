import {useMemo, useState} from "react";
import './Calculator.css';

function Calculator() {
    const [expression, setExpression] = useState('')
    const [result, setResult] = useState('')
    const [isError, setIsError] = useState(false)


    const isErrorClass = useMemo(() => {
        if (isError) {
            return 'error'
        }
        return ''
    }, [isError])

    const handleChange = (event) => {
        setExpression(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()

        fetch(
            'http://localhost:8000/process',
            {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    expression
                })
            }

        ).then((response) => {
            if (response.status === 200) {
                response.json().then((data) => {
                    setIsError(false)
                    setResult(data.result)
                })
            } else {
                response.json().then((data) => {
                    setIsError(true)
                    setResult(data.detail)
                })
            }

        }).catch((error) => {
            console.log({error})
            setIsError(true)
            setResult(`${error}`)
        })

    }

    return (
        <>
        <form onSubmit={handleSubmit}>
            <label>Enter your RPN expression:
                <input
                    type="text"
                    value={expression}
                    onChange={handleChange}
                    />
            </label>
            <input type="submit"/>
        </form>
        <div className={`result ${isErrorClass}`}>
            <span className="result-label">Result:</span><span>{result}</span>
        </div>
        </>
    )

}

export default Calculator;