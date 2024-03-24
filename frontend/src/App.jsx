import { useState } from 'react'
import busSyncLogo from './assets/logo.webp'
import './App.css'
function Logo() {
	return (
		<>
			<div>
				<img src={busSyncLogo} className='logo' alt='Bus-Sync logo' />
			</div>
		</>
	)
}

function App() {
	return (
		<>
			<Logo />
			<div className='login'>
				<label for=''>Login</label>
				<input type='text'></input>
				<br />
				<label for=''>Password</label>
				<input type='text'></input>
			</div>
		</>
	)
}

export default App
