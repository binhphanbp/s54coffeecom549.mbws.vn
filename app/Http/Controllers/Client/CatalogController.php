<?php

namespace App\Http\Controllers\Client;

use App\Http\Controllers\Controller;
use App\Models\Category;
use App\Services\Catalog\ProductQueryService;
use Illuminate\Http\Request;
use Illuminate\View\View;

class CatalogController extends Controller
{
    public function __construct(
        private readonly ProductQueryService $productQuery,
    ) {}

    public function index(Request $request): View
    {
        $categories = Category::where('is_active', true)
            ->where('is_draft', false)
            ->orderBy('sort_order')
            ->get();

        $filters = $request->only(['category', 'brand', 'q', 'min_price', 'max_price', 'sort_by']);

        $products = $this->productQuery
            ->listing($filters)
            ->with(['images', 'variants', 'category'])
            ->paginate(12)
            ->withQueryString();

        return view('client.catalog.index', compact('products', 'categories'));
    }

    public function show(string $locale, string $slug): View
    {
        $product = $this->productQuery->findActiveDetail($slug);

        if (! $product) {
            abort(404);
        }

        return view('client.catalog.product', compact('product'));
    }
}
