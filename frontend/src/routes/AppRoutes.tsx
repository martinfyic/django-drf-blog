import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Navbar } from '../ui';
import { HomePage } from '../blog';

export const AppRoutes = () => {
	return (
		<>
			<BrowserRouter>
				<Navbar />
				<Routes>
					<Route path="/" element={<HomePage />} />
				</Routes>
			</BrowserRouter>
		</>
	);
};
