<?php

namespace App\Http\Controllers\Client;

use App\Http\Controllers\Controller;
use App\Services\Catalog\ProductQueryService;
use Illuminate\View\View;

class HomeController extends Controller
{
    public function __construct(
        private readonly ProductQueryService $productQuery,
    ) {}

    public function index(): View
    {
        $featuredProducts = $this->productQuery
            ->listing()
            ->with(['images', 'variants', 'category'])
            ->take(8)
            ->get();

        return view('client.pages.home', compact('featuredProducts'));
    }
}
