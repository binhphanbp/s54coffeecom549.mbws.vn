<!doctype html>
<html lang="{{ app()->getLocale() }}">
<head>
    @include('client.partials.head')
</head>
<body class="s54-theme">
    @include('client.partials.header')

    <main role="main" class="o-main" id="MainContent">
        @yield('content')
    </main>

    @include('client.partials.footer')
    @include('client.partials.cart-drawer')

    {{-- Admin Toolbar & Inline Editing Hooks --}}
    @include('client.partials.admin-bar')
    @include('client.partials.inline-blocks')
    @include('client.partials.inline-outline')

    <script src="{{ asset('client-assets/js/vendor.js') }}"></script>
    <script src="{{ asset('client-assets/js/layouts.theme.js') }}"></script>
    <script src="{{ asset('client-assets/js/main.js') }}"></script>
    <script src="{{ asset('client-assets/js/client-cart.js') }}"></script>
    @stack('scripts')
</body>
</html>
