import axios from 'axios';

export const getBlogs = (url: string, setBlogs: React.Dispatch<React.SetStateAction<never[]>>) => {
	axios
		.get(url)
		.then((response) => {
			setBlogs(response.data);
		})
		.catch((error) => {
			console.log(error);
		});
};
