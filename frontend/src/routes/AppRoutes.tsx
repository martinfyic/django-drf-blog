import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Navbar, Footer } from '../ui';
import { HomePage, BlogItem } from '../blog';

export const AppRoutes: React.FC = () => {
	return (
		<>
			<BrowserRouter>
				<Navbar />
				<Routes>
					<Route path="/" element={<HomePage />} />
					<Route path="/blog/:slug" element={<BlogItem />} />
					<Route path="*" element={'404 | Not found'} />
				</Routes>
				<Footer />
			</BrowserRouter>
		</>
	);
};
