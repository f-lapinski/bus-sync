import './LoginForm.css'

export default function LoginForm() {
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
