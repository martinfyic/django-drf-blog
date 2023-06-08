import { Blog, BlogsProps } from '../interfaces';

export const Blogs: React.FC<BlogsProps> = ({ blogs }) => {
	return (
		<>
			<article className="grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 auto-rows-fr content-center">
				{blogs?.map((blog: Blog) => (
					<div className="bg-zinc-700 rounded-lg shadow p-4" key={blog.slug}>
						<h4 className="text-lg font-semibold mb-2">{blog.title}</h4>
						<h5 className="mb-5">
							<span>{blog.author}</span> | {blog.date_created}
						</h5>
						<p>{blog.overview}</p>
					</div>
				))}
			</article>
		</>
	);
};
