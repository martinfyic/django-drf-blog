import axios from 'axios';
import { Blog } from '../interfaces';

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

export const getOneBlog = (url: string, setBlog: React.Dispatch<React.SetStateAction<Blog>>) => {
	axios
		.get(url)
		.then((response) => {
			setBlog(response.data);
		})
		.catch((error) => {
			console.log(error);
		});
};
