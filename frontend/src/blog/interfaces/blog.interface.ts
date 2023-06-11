export interface Category {
	id: number;
	title: string;
	date_created: string;
	date_updated: string;
	thumbnail: string | null;
}

export interface Blog {
	author: number;
	categories: Category[];
	content: string;
	date_created: string;
	date_updated: string;
	feature: boolean;
	id: number;
	overview: string;
	slug: string;
	thumbnail: string;
	title: string;
}

export interface ResponseBlogAxios {
	count: number;
	next: string | null;
	previous: string | null;
	results: Blog[];
}

export type BlogsProps = {
	blogs: ResponseBlogAxios | undefined;
};
