import axios from 'axios';
import { Blog } from '..';

export const getBlogs = (url: string, setBlogs: React.Dispatch<React.SetStateAction<Blog[]>>) => {
	axios
		.get(url)
		.then((response) => {
			setBlogs(response.data);
		})
		.catch((error) => {
			console.log(error);
		});
};
