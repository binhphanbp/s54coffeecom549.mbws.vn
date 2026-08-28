<?php

namespace App\Http\Controllers\Client;

use App\Http\Controllers\Controller;
use App\Models\Page;
use Illuminate\View\View;

class PageController extends Controller
{
    public function show(string $locale, string $slug): View
    {
        if ($slug === 'our-story') {
            return view('client.pages.our-story');
        }

        if ($slug === 'wholesale') {
            return view('client.pages.wholesale');
        }

        $page = Page::where('slug', $slug)
            ->where('is_active', true)
            ->first();

        if ($page) {
            return view('client.pages.show', compact('page'));
        }

        abort(404);
    }
}
