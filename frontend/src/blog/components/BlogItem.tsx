import { useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { getOneBlog } from '../helpers';
import { Blog } from '../interfaces';

export const BlogItem = () => {
	const { slug } = useParams();
	const navigation = useNavigate();
	const URL = `http://127.0.0.1:8000/blog/get/${slug}`;

	const onNavigateBack = () => {
		navigation(-1);
	};

	const [blog, setBlog] = useState<Blog>({} as Blog);

	const memoizedGetOneBlog = useMemo(() => getOneBlog, []);

	useEffect(() => {
		memoizedGetOneBlog(URL, setBlog);
	}, [URL, memoizedGetOneBlog]);

	return (
		<div className="text-center mt-5">
			<h1 className="font-bold">{blog.title}</h1>
			<h4 className="font-bold mt-5">{blog.date_created}</h4>
			<p className="px-10 mx-auto max-w-5xl my-7">{blog.content}</p>
			<button className="bg-sky-700 px-4 py-2 rounded-xl hover:bg-sky-500 mt-2" onClick={onNavigateBack}>
				Volver
			</button>
		</div>
	);
};
