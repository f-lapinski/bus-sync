import busSyncLogo from '../../assets/logo.webp'
import './Logo.css'

export default function Logo() {
	return (
		<>
			<div>
				<img src={busSyncLogo} className='logo' alt='Bus-Sync logo' />
			</div>
		</>
	)
}
