import { useEffect, useState } from 'react';
import { Blog } from '../interfaces';
import { getBlogs } from '../helpers';

const URL = 'http://127.0.0.1:8000/blog/get';

export const HomePage = () => {
	const [blogs, setBlogs] = useState([]);

	useEffect(() => {
		getBlogs(URL, setBlogs);
	}, []);

	return (
		<>
			<h1 className="mt-9 text-center text-3xl font-bold ">Blog - Frontend</h1>
			<h2 className="mt-4 text-center text-2xl font-semibold">React Js + Django REST Framework</h2>
			<p className="mt-6 text-center px-12">
				Lorem ipsum dolor sit, amet consectetur adipisicing elit. Neque porro distinctio totam et repellendus aut
				deserunt sapiente delectus inventore odit animi quam ipsum recusandae, quia reprehenderit quae magni pariatur
				culpa rem. Accusantium fuga sapiente nostrum sequi. Consectetur minus ducimus nostrum quo perspiciatis aliquam
				perferendis quibusdam vero, consequatur rem aperiam expedita tempore? Velit hic aliquam quam, inventore
				molestias unde similique, omnis quasi alias earum sunt cumque!
			</p>
			<section>
				<h3>Blogs</h3>
				<ul>
					{blogs?.map((blog: Blog) => (
						<li key={blog.slug}>
							<h4>{blog.title}</h4>
							<h5>
								<span>{blog.author}</span> fecha: 02/20/2022
							</h5>
							<p>{blog.content}</p>
						</li>
					))}
				</ul>
			</section>
		</>
	);
};
