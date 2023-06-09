import { Link } from 'react-router-dom';
import { Blog, BlogsProps } from '../interfaces';

export const BlogList: React.FC<BlogsProps> = ({ blogs }) => {
	return (
		<>
			<article className="flex flex-wrap container mt-20 gap-6">
				{blogs?.map((blog: Blog) => (
					<Link to={`/blog/${blog.slug}`} key={blog.slug} className="w-full p-4">
						<div className="bg-zinc-700 rounded-lg shadow p-4 h-full max-w-5xl mx-auto">
							<h4 className="text-lg font-semibold mb-2">{blog.title}</h4>
							<h5 className="mb-5">
								<span>{blog.author}</span> | {blog.date_created}
							</h5>
							<p>
								{blog.categories.map((t) => (
									<strong className="mx-2">{t.title}</strong>
								))}
							</p>
							<p>{blog.overview}</p>
						</div>
					</Link>
				))}
			</article>
		</>
	);
};
