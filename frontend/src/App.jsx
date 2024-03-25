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

export function LoginForm() {
	return (
		<>
			<form action=''>
				<div className='login-form'>
					<div className='login-input'>
						<input type='text' placeholder='Login'></input>
					</div>
					<div className='password-input'>
						<input type='password' placeholder='Password'></input>
					</div>
					<div className='submit-button'>
						<button type='submit'>Log in</button>
					</div>
				</div>
				<p className='login-information'>You are don't have account? Contact with your administrator.</p>
			</form>
		</>
	)
}

function App() {
	return (
		<>
			<Logo />
			<LoginForm />
		</>
	)
}

export default App
